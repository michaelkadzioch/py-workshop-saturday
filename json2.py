import json

def main():
    data = {
            "name": "John Doe", 
            "age": 30, 
            "city": "New York"
            }
    
    print(data)

    # convert dictionary to JSON string
    jsonData = json.dumps(data)
    print(jsonData)


if __name__ == '__main__':
    main()