from flask import Flask, request, json, Response
from Dhelp import DataHelp

#   Пользователь обращается к API
#   1 Получение всех данных
#   2 Получение данных какого-то года
#   3 Получение данных года и месяца
#   4 Получение данных какого-то бизнеса
#   5 Мы создаем метод который будет использовать все параметры


d = DataHelp()


app = Flask("API_1")
app.config["JSON_AS_ASCII"] = False


@app.route("/test", methods=["GET"])
def t():
    return "Hello!!! I am working!!! :)))))))))"


@app.route("/api/v1/search", methods=["GET"])
def search():
    if "id" in request.args:
        id = int(request.args["id"])
        return {"id": id, "name": str(id) + ":the is"}
    return {"id": 200, "name": "test"}


@app.route("/api/v1/income", methods=["GET"])
def incomes():
    year = -1
    month = ""
    business = ""
    startperiod = -1
    endperiod = -1

    if "startperiod" in request.args:
        startperiod = int(request.args["startperiod"])

    if "endperiod" in request.args:
        endperiod = int(request.args["endperiod"])

    if "year" in request.args:
        year = int(request.args["year"])
    if "month" in request.args:
        month = str(request.args["month"])
    if "business" in request.args:
        business = str(request.args["business"])

    query = "select year, month, business.name as business, income from chema.finances left join chema.business on business.id=business"

    notfirst = False

    if (
        startperiod != -1
        or endperiod != -1
        or year != -1
        or month != ""
        or business != ""
    ):
        query = query + " where "
        for arg in request.args:
            if (
                arg != "startperiod"
                and arg != "endperiod"
                and arg != "year"
                and arg != "month"
                and arg != "business"
            ):
                continue
            if notfirst:
                query = query + " and "

            s = request.args[arg]
            if arg == "startperiod":
                query = query + f"year between {s}"
            if arg == "endperiod":
                query = query + f" {s}"

            if arg == "year":
                query = query + f" year = {s}"
            if arg == "month":
                query = query + f" month = '{s}'"
            if arg == "business":
                query = query + f" business.name = '{s}'"
            notfirst = True
    response = Response(
        json.dumps(d.executeSomeQuery(query)),
        content_type="application/json; charset=utf-8",
    )
    return response


app.run()
