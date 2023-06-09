result = []


def divider(a, b):
    try:
        if a < b:
            raise ValueError
        if b > 100:
            raise IndexError
        return a / b
    except ValueError:
        print("Помилка: a < b")
    except IndexError:
        print("Помилка: b > 100")
    except Exception as e:
        print("Інша помилка:", type(e).__name__)


data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
