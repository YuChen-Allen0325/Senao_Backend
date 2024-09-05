API Document:<br>
<br>
  The project had completed by using Django Restframework.<br>
  Two APIs are in the redirection > views.py.<br>
<br>
  **API 1: Create Short URL**   (using POST method)<br><br>
    Input (payload):<br>
      "original_url": the url you want to shorten<br><br>
    Output:<br>
      "short_url": the url is original_url shortened url and a null character indicates conversion failure<br>
      "expiration_date": the timestamp is represented expiration date and a null character indicates conversion failure<br>
      "success": A boolean field indicating whether the URL was successfully shortened.<br>
      "reason": reason for failure , some are made of module exception<br><br><br>
<br>
  **API 2: Redirect Using Short URL**   (using GET method)<br><br>
    the short_url directly redirect to original_url , no parameters required<br>
