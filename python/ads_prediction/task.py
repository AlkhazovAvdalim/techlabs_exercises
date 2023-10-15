# Challenge 3: Implement Ads Click prediction!

# Replace the email string with the email you used to register for Techlabs!
# This is required to generated your submission key.
EMAIL = "max_mustermann@gmail.com"

def transform(data):
    # TODO: Implement me!
    # This function receives the a dataset as a pandas dataframe and should return a transformed dataframe
    # You can use this function to perform normalizations or any data preprocessing you want!
    return data

def train(traindata): 
    # TODO: Implement me!
    # Implement any model you want but don't go to crazy with the complexity!
    # This function should return a model that can be used for prediction. 
    # It will receive the data after transformation by the `transform` function
    return None


def predict(model, data):
    # TODO: Implement me!
    # This funciton should return the predictions for a dataframe `data`
    # `model` will be the Model return by your `train` function
    # Note that data will already be transformed by the `transform` function
    return None

if __name__ == "__main__":
    import base64
    eval(compile(base64.b64decode("ZGVmIFRMX05TX19nZW5LZXkocGFzc3BocmFzZSwgc2VjcmV0KToKICAgIGltcG9ydCBiYXNlNjQKICAgIHN1cGVyX3NlY3JldCA9ICJDQVRDSF9tZV9pZl95b3VfY2FuIUJ1dF9ZT1VfV09OVCFCZWNhdXNlX3RoaXNfaXMhU1VQRVJfU0VDUkVUISIKICAgIGtleSA9IGJ5dGVzKGEgXiBiICBmb3IgYSwgYiBpbiB6aXAocGFzc3BocmFzZS5lbmNvZGUoKSwgc3VwZXJfc2VjcmV0LmVuY29kZSgpKSkKICAgIGtleSA9IGJ5dGVzKGEgXiBiIGZvciBhLCBiIGluIHppcChrZXksIHNlY3JldC5lbmNvZGUoKSkpCiAgICBrZXkgPSBiYXNlNjQudXJsc2FmZV9iNjRlbmNvZGUoa2V5KQogICAgcmV0dXJuIGtleS5kZWNvZGUoKQoKZGVmIFRMX05TX19nZXRfZGF0YShkYXRhX3BhdGg9X19maWxlX18pOgogICAgaW1wb3J0IHBhbmRhcyBhcyBwZAogICAgdHJhaW5fY3N2ID0gcGQucmVhZF9jc3YoZiJ7ZGF0YV9wYXRofS9hZHNfdHJhaW5kYXRhLmNzdiIpCiAgICB0ZXN0X2NzdiA9IHBkLnJlYWRfY3N2KGYie2RhdGFfcGF0aH0vYWRzX3Rlc3RkYXRhLmNzdiIpCiAgICByZXR1cm4gdHJhaW5fY3N2LCB0ZXN0X2NzdgoKZGVmIFRMX05TX19ldmFsKGNsZiwgdGVzdCk6CiAgICBmcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgY29uZnVzaW9uX21hdHJpeAogICAgbWF0cml4ID0gY29uZnVzaW9uX21hdHJpeCh0ZXN0WyJQdXJjaGFzZWQiXSwgcHJlZGljdChjbGYsIHRlc3QpKQogICAgZXJyb3JzID0gbWF0cml4WzBdWzFdICsgbWF0cml4WzFdWzBdCiAgICByZXR1cm4gZXJyb3JzCgoKZGVmIFRMX05TX19jaGVjayhkYXRhX3BhdGg9X19maWxlX18pOgogICAgaW1wb3J0IG9zCiAgICBpbXBvcnQgcGFuZGFzIGFzIHBkCiAgICBkYXRhX3BhdGggPSBvcy5wYXRoLmRpcm5hbWUoZGF0YV9wYXRoKQogICAgdHJhaW5kcywgdGVzdGRzID0gVExfTlNfX2dldF9kYXRhKGRhdGFfcGF0aCkKICAgIHRyYWluZHMgPSB0cmFuc2Zvcm0odHJhaW5kcykKICAgIHRlc3RkcyA9IHRyYW5zZm9ybSh0ZXN0ZHMpCiAgICBtb2RlbCA9IHRyYWluKHRyYWluZHMpCgogICAgZXJyb3JzID0gVExfTlNfX2V2YWwobW9kZWwsIHRlc3RkcykKCiAgICBwcmludChmIkZhbHNlLXBvc2l0aXZlcy9mYWxzZS1uZWdhdGl2ZXM6IHtlcnJvcnN9IikKICAgIGlmIGVycm9ycyA+IDUgYW5kIGVycm9ycyA8IDEwOgogICAgICAgIHNlY3JldCA9IFRMX05TX19nZW5LZXkoRU1BSUwsICJuaWNlX3lvdV9nb3RfdGhlX3JpZ2h0X2tleSIpCiAgICAgICAgcHJpbnQoZiJDb25ncmF0dWxhdGlvbnMhIFlvdSBhY2hpZXZlIGFuIGFjY2VwdGFibGUgbW9kZWwgcGVyZm9ybWFuY2UuIFlvdXIgc2VjcmV0IGtleSBpcyB7c2VjcmV0fSIpCiAgICAgICAgcmV0dXJuCiAgICBlbGlmIGVycm9ycyA+PSAxMDoKICAgICAgICBwcmludChmIllvdXIgbW9kZWwgcGVyZm9ybWFuY2UgaXMgbm90IGdvb2QgZW5vdWdoISBUcnkgYWdhaW4gcGxzLi4uIikKICAgICAgICByZXR1cm4KICAgIGVsc2U6CiAgICAgICAgcHJpbnQoZiJZb3VyIG1vZGVsIHBlcmZvcm1hbmNlIGlzIGdvb2QsIHRvbyBnb29kID8hIChJZiB5b3UgZGlkIG5vdCBjaGVhdCwgcGxlYXNlIGNvbnRhY3QgdXMgb24gc2xhY2spIikKICAgICAgICByZXR1cm4KVExfTlNfX2NoZWNrKCk="), "<string>", "exec"))
