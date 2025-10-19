# 1. основний текстовий файл
with open('test_salaries.txt', 'w', encoding='utf-8') as f:
    f.write('Alex Korp,3000\n')
    f.write('Nikita Borisenko,2000\n')
    f.write('Sitarama Raju,1000\n')

# 2. обчислення загальної та середньої зарплати
def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропустити порожні рядки
                try:
                    _, salary = line.split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"⚠️ Помилка у рядку: {line}")
                    continue  # пропустити некоректний рядок
            if count == 0:
                return (0, 0)
            average = total / count
            return total, average
    except FileNotFoundError:
        print(f"❌ Файл за шляхом '{path}' не знайдено.")
        return None
    except Exception as e:
        print(f"❌ Сталася помилка: {e}")
        return None

# 3. Тестовий виклик функції
result = total_salary('test_salaries.txt')
if result:
    print("✅ Загальна сума зарплат:", result[0])
    print("✅ Середня зарплата:", result[1])
