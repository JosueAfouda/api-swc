import sqlite3

def create_database():
    db_name = "fantasy_data.db"
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Création des tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS player (
            player_id INTEGER NOT NULL PRIMARY KEY,
            gsis_id VARCHAR,
            first_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL,
            position VARCHAR NOT NULL,
            last_changed_date DATE NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance (
            performance_id INTEGER NOT NULL PRIMARY KEY,
            week_number VARCHAR NOT NULL,
            fantasy_points FLOAT NOT NULL,
            player_id INTEGER NOT NULL,
            last_changed_date DATE NOT NULL,
            FOREIGN KEY(player_id) REFERENCES player (player_id)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS league (
            league_id INTEGER NOT NULL PRIMARY KEY,
            league_name VARCHAR NOT NULL,
            scoring_type VARCHAR NOT NULL,
            last_changed_date DATE NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS team (
            team_id INTEGER NOT NULL PRIMARY KEY,
            team_name VARCHAR NOT NULL,
            league_id INTEGER NOT NULL,
            last_changed_date DATE NOT NULL,
            FOREIGN KEY(league_id) REFERENCES league (league_id)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS team_player (
            team_id INTEGER NOT NULL,
            player_id INTEGER NOT NULL,
            last_changed_date DATE NOT NULL,
            PRIMARY KEY (team_id, player_id),
            FOREIGN KEY(team_id) REFERENCES team (team_id),
            FOREIGN KEY(player_id) REFERENCES player (player_id)
        )
    """)
    
    # Valider et fermer la connexion
    conn.commit()
    conn.close()
    print(f"Database '{db_name}' created successfully with all tables.")

if __name__ == "__main__":
    create_database()
