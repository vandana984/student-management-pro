"""
Test Neon PostgreSQL Connection
Reads API key from tokens file and tests the database connection.
"""
import urllib.request
import json
import ssl
import sys
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Read Neon API token from tokens file
def get_neon_token():
    with open("../tokens", "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("Neon"):
            # Token value is 2 lines after "Neon"
            token_line = lines[i + 2].strip()
            return token_line.replace("Token Value ", "").strip()
    raise Exception("Neon token not found in tokens file")

def neon_api_request(endpoint, token, method="GET"):
    """Make a request to the Neon API"""
    url = f"https://console.neon.tech/api/v2/{endpoint}"
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx) as response:
        return json.loads(response.read().decode())

def main():
    print("=" * 50)
    print("  Neon PostgreSQL Connection Test")
    print("=" * 50)
    
    # Step 1: Read token
    print("\n[1/4] Reading Neon API token from tokens file...")
    try:
        token = get_neon_token()
        print(f"  [OK] Token found: {token[:10]}...{token[-5:]}")
    except Exception as e:
        print(f"  [FAIL] {e}")
        return
    
    # Step 2: List projects
    print("\n[2/4] Fetching Neon projects...")
    try:
        data = neon_api_request("projects", token)
        projects = data.get("projects", [])
        if not projects:
            print("  [WARN] No projects found.")
            return
        project = projects[0]
        project_id = project["id"]
        print(f"  [OK] Project: {project['name']} (ID: {project_id})")
        print(f"       Region: {project.get('region_id', 'N/A')}")
        print(f"       PG Version: {project.get('pg_version', 'N/A')}")
    except Exception as e:
        print(f"  [FAIL] {e}")
        return
    
    # Step 3: Get connection URI
    print("\n[3/4] Fetching connection URI...")
    try:
        conn_data = neon_api_request(
            f"projects/{project_id}/connection_uri?database_name=neondb&role_name=neondb_owner",
            token
        )
        conn_uri = conn_data.get("uri", "")
        # Mask password in display
        masked = conn_uri
        if "@" in conn_uri and ":" in conn_uri:
            parts = conn_uri.split("@")
            user_pass = parts[0]
            colon_idx = user_pass.rfind(":")
            masked = user_pass[:colon_idx] + ":****@" + parts[1]
        print(f"  [OK] Connection URI: {masked}")
    except Exception as e:
        print(f"  [FAIL] {e}")
        return
    
    # Step 4: Test actual database connection
    print("\n[4/4] Testing database connection...")
    try:
        import psycopg2
        conn = psycopg2.connect(conn_uri)
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        cursor.execute("SELECT current_database(), current_user;")
        db_info = cursor.fetchone()
        cursor.close()
        conn.close()
        
        print(f"  [OK] CONNECTION SUCCESSFUL!")
        print(f"       PostgreSQL: {version}")
        print(f"       Database:   {db_info[0]}")
        print(f"       User:       {db_info[1]}")
    except ImportError:
        print("  [WARN] psycopg2 not installed.")
        print("  Run: python -m pip install psycopg2-binary")
        return
    except Exception as e:
        print(f"  [FAIL] Database connection failed: {e}")
        return
    
    print("\n" + "=" * 50)
    print("  All Tests Passed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
