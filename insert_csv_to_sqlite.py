import sqlite3
import csv

def enable_foreign_keys(conn):
    """Active les clés étrangères."""
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.commit()

def import_csv_to_table(conn, csv_file, table_name):
    """Importe un fichier CSV dans une table SQLite."""
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Ignore la première ligne (en-têtes)
        placeholders = ', '.join(['?' for _ in headers])  # Génère ?, ?, ? ...
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        
        cursor = conn.cursor()
        cursor.executemany(query, reader)
        conn.commit()
    print(f"Données importées dans {table_name} depuis {csv_file}")

def verify_data_counts(conn):
    """Vérifie le nombre d'enregistrements dans chaque table."""
    tables = [
        ("player", None),
        ("performance", None),
        ("performance", "WHERE last_changed_date > '2024-04-01'"),
        ("league", None),
        ("team", None),
        ("team_player", None)
    ]
    
    cursor = conn.cursor()
    for table, condition in tables:
        query = f"SELECT COUNT(*) FROM {table}"
        if condition:
            query += f" {condition}"
        cursor.execute(query)
        count = cursor.fetchone()[0]
        print(f"{table}: {count} enregistrements")

def main():
    db_name = "fantasy_data.db"
    conn = sqlite3.connect(db_name)
    enable_foreign_keys(conn)
    
    csv_files = {
        "data/player_data.csv": "player",
        "data/performance_data.csv": "performance",
        "data/league_data.csv": "league",
        "data/team_data.csv": "team",
        "data/team_player_data.csv": "team_player"
    }
    
    for csv_file, table_name in csv_files.items():
        import_csv_to_table(conn, csv_file, table_name)
    
    verify_data_counts(conn)
    conn.close()
    print("Importation terminée. Connexion SQLite fermée.")

if __name__ == "__main__":
    main()
