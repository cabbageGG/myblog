from rest_framework.response import Response

def NormalResponse(result):
    data = {
        "status":2000,
        "message":"success",
        "result":result,
        "mudule":"blog"
    }
    return Response(data=data)