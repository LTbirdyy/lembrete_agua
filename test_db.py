from src.interface.services.db import get_supabase

supabase = get_supabase()

resultado = supabase.table("historico").select("*").execute()

print(resultado.data)