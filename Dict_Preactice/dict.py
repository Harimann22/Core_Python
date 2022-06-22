keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res = dict(zip(keys, values))
print(res)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])
