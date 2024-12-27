import azure.functions as func
import logging

from tt.handle_event import handle_event

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="thot_terminator_endpoint")
def thot_terminator_endpoint(req: func.HttpRequest) -> func.HttpResponse:
    """
    This endpoint accepts a POST request with:
    
    :param user_id: The user's twitter ID
    :param message: The message the user sent us 
    """
    logging.info('Python HTTP trigger function processed a request.')

    user_id = req.params.get('user_id')
    message = req.params.get('message')
    if not user_id or not message:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            user_id = req_body.get('user_id')
            message = req_body.get('message')

    if user_id and message:
        return handle_event(user_id, message)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
