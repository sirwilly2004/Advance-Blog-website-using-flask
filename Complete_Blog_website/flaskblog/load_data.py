import json
from your_application import db, Post  # Adjust the import based on your app structure

def load_data_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def insert_data_to_db(data):
    for item in data:
        post = Post(
            title=item['title'],
            content=item['content'],
            user_id=item['user_id']
        )
        db.session.add(post)
    
    db.session.commit()  # Commit all changes to the database

if __name__ == "__main__":
    json_data = load_data_from_json('data.json')  # Path to your JSON file
    insert_data_to_db(json_data)
    print("Data inserted successfully!")
