#Bot that sends random pic of a dog
import telebot
import requests
API_TOKEN = 'Enter your token'
bot = telebot.TeleBot(API_TOKEN)
def get_random_dog_image():
    response = requests.get("https://random.dog/woof.json")
    if response.status_code == 200:
        data = response.json()
        return data["url"]
    return None
@bot.message_handler(commands=['random'])
def send_random_dog(message):
    dog_image_url = get_random_dog_image()
    if dog_image_url:
        bot.send_photo(message.chat.id, dog_image_url)
    else:
        bot.send_message(message.chat.id, "Не удалось получить изображение собаки.")
if __name__ == '__main__':
    bot.polling(none_stop=True)
