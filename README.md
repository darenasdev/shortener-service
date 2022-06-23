# Shortener-service


Before run, change api_key variable into api/main.py file


## Build docker image

Use the following command to build image 

````bash
    $ docker build -t <YOUR_TAG> .
````

## Request example
- {BASE_URL}/api/v1/unshort_url/:
    ```bash
        $ curl -X POST -d '{"short_url": "http://bit.ly/cXEInp"}' {BASE_URL}/api/v1/unshort_url/ | jq

        {
            "long_url": "https://www.flickr.com/photos/26432908@N00/346615997/sizes/l/",
            "message": "success",
            "short_url": "http://bit.ly/cXEInp"
        }
    ```
- {BASE_URL}/api/v1/generate_url/:
    ```bash
        $ curl -X POST -d '{"long_url": "https://dev.bitly.com"}' {BASE_URL}/api/v1/generate_url/ | jq
        {
            "long_url": "https://dev.bitly.com",
            "message": "success",
            "short_url": "https://bitly.is/3QqwvFY"
        }
    ```