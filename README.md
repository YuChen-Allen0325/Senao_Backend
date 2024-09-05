# API Document:<br>
<br>
  The project had completed by using Django Restframework.<br>
  Two APIs are in the redirection > views.py.<br>
<br>
  **API 1: Create Short URL**   (using POST method)<br><br>
    Input (payload):<br>
      "original_url": the url you want to shorten<br>
      ![201](https://github.com/user-attachments/assets/805adf03-02b5-406a-9ee5-ba1e0ad257f5)
      <br><br>
    Output:<br>
      "short_url": the url is original_url shortened url and a null character indicates conversion failure<br>
      "expiration_date": the timestamp is represented expiration date and a null character indicates conversion failure<br>
      "success": A boolean field indicating whether the URL was successfully shortened.<br>
      "reason": reason for failure , some are made of module exception<br>
      ![201-1](https://github.com/user-attachments/assets/4cc891b9-09f1-4f2f-8603-0a8e40e2090a)
      <br><br>
    status code:<br>
      201: the short_url is created and conversion successful<br>
      400: error occur<br>
      429: indicates that the user has sent too many requests in a given amount of time and is being rate-limited or throttled<br><br>
    error message:<br>
      "original_url is required": original_url is not in payload<br>
      "original_url must be a string" original_url is not str type<br>
      "URL too long": original_url is exceed 2048 char<br>
      "Invalid URL": original_url is not a accessible website<br>
      "Failed to parse: 'www.google.com..tw', label empty or too long": domain name does not conform to the expected format for valid domain names or URLs<br>
      "HTTPSConnectionPool(host='your_original_url', port=443): Max retries exceeded with url: / (Caused by NameResolutionError(\"<urllib3.connection.HTTPSConnection object at 0x7f3ae34b7bb0>: Failed to resolve 'your_original_url' ([Errno -2] Name or service not known)\"))": the domain name cannot be found or resolved to an IP address.<br><br><br>
<br>
  **API 2: Redirect Using Short URL**   (using GET method)<br><br>
    the short_url directly redirect to original_url , no parameters required<br><br>
    status code:<br>
      200: redirect short URL to original_url and succeed<br>
      302: redirection to original_url<br>
      404: short_url not found<br>
      410: short_url is expired<br><br>
    error message:<br>
      "URL not found": the short_url not in database
      "URL expired": the short_url is expired

# User guide:<br>
