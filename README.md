API Document:

  The project had completed by using Django Restframework.
  Two APIs are in the redirection > views.py.

  API 1: Create Short URL   (using POST method)
    Input (payload):
      "original_url": the url you want to shorten
    Output:
      "short_url": the url is original_url shortened url and a null character indicates conversion failure
      "expiration_date": the timestamp is represented expiration date and a null character indicates conversion failure
      "success": A boolean field indicating whether the URL was successfully shortened.
      "reason": reason for failure , some are made of module exception
  
  API 2: Redirect Using Short URL   (using GET method)
    the short_url directly redirect to original_url , no parameters required
