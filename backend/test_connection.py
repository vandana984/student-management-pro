"""
Test Render API Connection
Reads API key from tokens file and tests the Render API connection.
"""
import urllib.request
import json
import ssl
import sys
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def get_render_token():
    """Read Render API token from tokens file"""
    with open("../tokens", "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("Render"):
            token_line = lines[i + 2].strip()
            return token_line.replace("Token Value ", "").strip()
    raise Exception("Render token not found in tokens file")

def render_api_request(endpoint, token):
    """Make a request to the Render API"""
    url = f"https://api.render.com/v1/{endpoint}"
    req = urllib.request.Request(url, method="GET")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/json")
    
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, context=ctx) as response:
        return json.loads(response.read().decode())

def main():
    print("=" * 50)
    print("  Render API Connection Test")
    print("=" * 50)
    
    # Step 1: Read token
    print("\n[1/3] Reading Render API token from tokens file...")
    try:
        token = get_render_token()
        print(f"  [OK] Token found: {token[:10]}...{token[-5:]}")
    except Exception as e:
        print(f"  [FAIL] {e}")
        return
    
    # Step 2: Check account
    print("\n[2/3] Checking Render account...")
    try:
        owners = render_api_request("owners", token)
        for o in owners:
            owner = o.get("owner", {})
            print(f"  [OK] Account verified!")
            print(f"       Name:  {owner.get('name', 'N/A')}")
            print(f"       Email: {owner.get('email', 'N/A')}")
            print(f"       Type:  {owner.get('type', 'N/A')}")
            print(f"       ID:    {owner.get('id', 'N/A')}")
    except Exception as e:
        print(f"  [FAIL] {e}")
        return
    
    # Step 3: Check services
    print("\n[3/3] Checking existing services...")
    try:
        services = render_api_request("services?limit=10", token)
        if not services:
            print("  [OK] No services yet (ready to deploy)")
        else:
            for s in services:
                svc = s.get("service", {})
                print(f"  - {svc.get('name', 'N/A')} ({svc.get('type', 'N/A')})")
    except Exception as e:
        print(f"  [FAIL] {e}")
        return
    
    print("\n" + "=" * 50)
    print("  All Tests Passed!")
    print("=" * 50)

if __name__ == "__main__":
    main()
