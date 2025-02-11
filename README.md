1. ```pip install fastapi uvicorn requests```
2. Put in your API key.
3. ```uvicorn main:app --reload```

## Example translation request:
```
curl -X 'POST' 'http://127.0.0.1:8000/translate' \
     -H 'Content-Type: application/json' \
     -d '{"text": "Hello, how are you?"}'
```
API response I got back:
```
{
    "translated_text": "Hei, miten saat? (Hello, how are you?)"
}
```

## Example sentiment analysis request:
```
curl -X 'POST' 'http://127.0.0.1:8000/sentiment' \
     -H 'Content-Type: application/json' \
     -d '{"text": "I am feeling great today!"}'
```
API response I got back:
```
{
    "sentiment": "I would classify the sentiment as POSITIVE."
}
```
