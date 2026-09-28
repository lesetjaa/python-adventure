# Notes

## Requests

- So far we know 1 request method which is the `get` request, there are three more requests methods namely:

1. Post
2. Put
3. Delete

```python
requests.get()
requests.post()
requests.put()
requests.delete()
```

### Post Request

- This is used to give the external system a piece of data but we are not interested in the response, just that if it was successful or not

### Put Request

- This is used to update a piece if data in the external system

### Delete Request

- Used for deleting a piece of data in the external system

### Headers

- Previously we made requests by adding parameters straight into our url, this is typically not safe as it is a bit more exposed to hackers and invadors.
- Headers hide this information by sending this data as behind-the-scenes alongside a web request or response
