""" Requests status codes constants"""
REQUEST_SUCCESS       = 200 # This is the standard “OK” status code for a successful HTTP request;
REQUEST_CREATED       = 201 # Typically, this is the status code that is sent after a POST/PUT request;
REQUEST_FULFILLED     = 204 # Examples of this status code include delete requests; 
REQUEST_BAD           = 400 # The server cannot understand and process a request due to a client error.
REQUEST_UNAUTHORIZED  = 401 # This status code request occurs when authentication is required but has failed or not been provided.
REQUEST_FORBIDDEN     = 403 # This happens if a client/user requires the necessary permission or they may need an account to access the resource.
REQUEST_NOT_FOUND     = 404 # A status code 404 occurs when the request is valid, but the resource cannot be found on the server. 
REQUEST_UPDATE_ERR    = 409 # This is usually an issue with simultaneous updates, or versions, that conflict with one another.
REQUEST_RESOURCE_MISS = 401 # Resource requested is no longer available and will not be available again.
REQUEST_SERVER_FAILED = 500 # The status code 500 happens when the server cannot fulfill a request due to an unexpected issue.

""" API urls defined"""
# DEVICE URLS
API_GET_DEVICE  = "/get-device/"
API_POST_DEVICE = "/create-device"
# CMD URLS
API_GET_CMDS     = "/get-cmd/"
API_UPDATE_CMD  = "/update-cmd-status/"

# URLOAD URLS
API_UPLOAD_DATA = "/upload/"

""" CMD TYPES defined"""
EXECUTABLE = 1
CMD        = 2
SELENIUM   = 3
INSTALLER  = 4
CUSTOM     = 5
SCREENSHOT = 6