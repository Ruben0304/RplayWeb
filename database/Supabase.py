from supabase import create_client, Client

url: str = "https://tnuvhxvelwizhieiiglq.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRudXZoeHZlbHdpemhpZWlpZ2xxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4OTgzMzI3NywiZXhwIjoyMDA1NDA5Mjc3fQ.D1sc8Qug8ua2nO0xf3_xJkp5Bx7bBP3ZS_snAwehODg"
supabase: Client = create_client(url, key)