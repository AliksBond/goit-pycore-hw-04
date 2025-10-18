with open('cats.txt', 'w', encoding='utf-8') as f:
    f.write('60b90c1c13067a15887e1ae1,Tayson,3\n')
    f.write('60b90c2413067a15887e1ae2,Vika,1\n')
    f.write('60b90c2e13067a15887e1ae3,Barsik,2\n')
    f.write('60b90c3b13067a15887e1ae4,Simon,12\n')
    f.write('60b90c4613067a15887e1ae5,Tessi,5\n')

# Зчитування інформації про котів з файлу
def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Пропуск порожніх рядкiв
                try:
                    cat_id, name, age = line.split(',')
                    cat = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats.append(cat)
                except ValueError:
                    print(f"⚠️ Некоректний рядок: {line}")
                    continue  # Пропуск неправильних рядкiв
        return cats
    except FileNotFoundError:
        print(f"❌ Файл '{path}' не знайдено.")
        return []
    except Exception as e:
        print(f"❌ Сталася помилка: {e}")
        return []

# Виклик 
cats_info = get_cats_info('cats.txt')

print("📋 Інформація про котів:")
for cat in cats_info:
    print(cat)
