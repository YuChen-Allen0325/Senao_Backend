API Document:<br>
<br>
  The project had completed by using Django Restframework.<br>
  Two APIs are in the redirection > views.py.<br>
<br>
  API 1: Create Short URL   (using POST method)<br>
    <p style="margin-left: 4em;">
    Input (payload):<br>
      <p style="margin-left: 2em;">
      "original_url": the url you want to shorten<br>
      </p>
    Output:<br>
      <p style="margin-left: 2em;">
      "short_url": the url is original_url shortened url and a null character indicates conversion failure<br>
      "expiration_date": the timestamp is represented expiration date and a null character indicates conversion failure<br>
      "success": A boolean field indicating whether the URL was successfully shortened.<br>
      "reason": reason for failure , some are made of module exception<br>
      </p>
    </p>
<br>
  API 2: Redirect Using Short URL   (using GET method)<br>
    the short_url directly redirect to original_url , no parameters required<br>
