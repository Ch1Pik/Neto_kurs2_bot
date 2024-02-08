    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        chat_id INTEGER);
        
     CREATE TABLE IF NOT EXISTS Words (
        word_id INTEGER PRIMARY KEY,
        word TEXT,
        translation text);
        
     CREATE TABLE IF NOT EXISTS UserWords (
        user_id INTEGER,
        word_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES Users(user_id),
        FOREIGN KEY(word_id) REFERENCES Words(word_id));
        
     CREATE TABLE IF NOT EXISTS TestResults (
        user_id INTEGER,
        word_id INTEGER,
        result INTEGER,
        FOREIGN KEY(user_id) REFERENCES Users(user_id),
        FOREIGN KEY(word_id) REFERENCES Words(word_id));
