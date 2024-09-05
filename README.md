# API Document:<br>
<br>
  The project had completed by using Django Restframework.<br>
  Two APIs are in the redirection > views.py.<br>
<br>
  **API 1: Create Short URL**   (using POST method)<br><br>
    Input (payload):<br>
      "original_url": the url you want to shorten<br>
      ![image](https://github.com/user-attachments/assets/d0260041-9f16-4660-ae22-f9329965e959)
      <br><br>
    Output:<br>
      "short_url": the url is original_url shortened url and a null character indicates conversion failure<br>
      "expiration_date": the timestamp is represented expiration date and a null character indicates conversion failure<br>
      "success": A boolean field indicating whether the URL was successfully shortened.<br>
      "reason": reason for failure , some are made of module exception<br>
      ![image](https://github.com/user-attachments/assets/699f5a1c-5d41-4a0a-8157-4dfce3673eaa)
      <br><br>
    status code:<br>
      201: the short_url is created and conversion successful<br>
      400: original_url is missing or original_url is not a string or 'requests' module raise excetion like "Failed to parse: 'www.google.com..tw', label empty or too long" and "HTTPSConnectionPool(host='www.google.com.tww', port=443): Max retries exceeded with url: / (Caused by NameResolutionError(\"<urllib3.connection.HTTPSConnection object at 0x7f3ae3348610>: Failed to resolve 'www.google.com.tww' ([Errno -2] Name or service not known)\"))"<br>
    
<br>
  **API 2: Redirect Using Short URL**   (using GET method)<br><br>
    the short_url directly redirect to original_url , no parameters required<br>



# User guide:<br>
