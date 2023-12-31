import azure.functions as func
import logging

app = func.FunctionApp()

# Learn more at aka.ms/pythonprogrammingmodel

# Get started by running the following code to create a function using a HTTP trigger.

@app.function_name(name="FncTeste")
@app.route(route="hello", auth_level = func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
     logging.info('Python HTTP trigger function processed a request.')

     name = req.params.get('name')
     if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

     if name:
        return func.HttpResponse(f"Buenas!! ^_^, {name}. This HTTP triggered function executed successfully!! (?).")
     else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully (?) **yep (^///^). Pass a name in the query string or in the request body for a personalized response!! or else.....",
             status_code=200
        )
