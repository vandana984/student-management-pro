import urllib.request
import json
import ssl
import psycopg2
import sys
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def get_neon_token():
    with open("../tokens", "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("Neon"):
            token_line = lines[i + 2].strip()
            return token_line.replace("Token Value ", "").strip()
    raise Exception("Neon token not found in tokens file")

def neon_api_request(endpoint, token):
    url = f"https://console.neon.tech/api/v2/{endpoint}"
    req = urllib.request.Request(url, method="GET")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx) as response:
        return json.loads(response.read().decode())

def apply_sql_file(conn, sql_file):
    with open(sql_file, 'r') as f:
        sql = f.read()
    
    with conn.cursor() as cursor:
        print(f"Applying: {sql_file}...")
        cursor.execute(sql)
        print(f"Success: Applied {sql_file}")

def main():
    try:
        token = get_neon_token()
        data = neon_api_request("projects", token)
        project_id = data["projects"][0]["id"]
        
        conn_data = neon_api_request(
            f"projects/{project_id}/connection_uri?database_name=neondb&role_name=neondb_owner",
            token
        )
        conn_uri = conn_data["uri"]
        
        conn = psycopg2.connect(conn_uri)
        conn.autocommit = True
        
        # Apply schema files
        apply_sql_file(conn, "schema/01_users.sql")
        
        conn.close()
        print("\n[OK] DATABASE SCHEMA APPLIED SUCCESSFULLY")
    except Exception as e:
        print(f"\n[FAIL] {e}")

if __name__ == "__main__":
    main()
