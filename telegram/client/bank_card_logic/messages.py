start_message = 'Выберете вопрос ниже ⬇'

card_cost_answer = '''
<b>{question}</b>

Стоимость проезда на маршруте с регулируемым тарифом при оплате БК установлена постановлением Правительства Московской области от 11.10.2022 № 1109/36. 

Стоимость проезда на городском маршруте равна 54 руб.

Стоимость проезда на маршруте с нерегулируемым тарифом при оплате БК соответствует тарифу перевозчика, установленного для данного маршрута.
'''

card_count_pay_answer = '''
<b>{question}</b>

При наличии в транспортном средстве стационарного оборудования (автоматического терминала, расположенного на поручне), оплатить проезд на одном рейсе одной БК можно за одного пассажира.
В случае регистрации проезда водителем на мобильном терминале, оплатить проезд на одном рейсе одной БК можно за двух пассажиров.
Оплатить проезд большего количества пассажиров можно дополнительно с использованием карты Стрелка, Тройка или другой БК.
'''

card_history_answer = '''
<b>{question}</b>

Эту информацию можно получить в Личном кабинете пассажира – специализированном интернет-портале, предназначенном для предоставления информации о поездках, просмотра истории регистрации поездок с использованием БК, а также иной информации.

Для входа в личный кабинет пройдите по ссылке
<a href="https://rrtp.ru/cards">Войти в Личный кабинет</a>

Если не увидели информацию по истории оплаты поездок в Личном кабинете - пройдите по <a href="https://securepayments.sberbank.ru/client/login">ссылке.</a>
'''

card_error_answer = '''
<b>{question}</b>

Если Ваша карта не принимается для оплаты проезда на терминале, даже если Вы успешно расплачивались этой картой ранее, это может быть следствием следующих причин:

Карта в стоп-листе. Это означает, что по данной карте была совершена поездка, за которую не произошло списание средств. Таким образом, поездка осталась неоплаченной, и по карте образовалась задолженность.

Это может произойти из-за недостатка средств на карте на момент оплаты, блокировки карты банком или технических проблем при выполнении запроса на списание средств. Попробуйте погасить задолженность через  <a href="https://rrtp.ru/cards">Личный кабинет пассажира.</a> Если не увидели информацию по истории оплаты поездок в Личном кабинете - пройдите по <a href="https://securepayments.sberbank.ru/client/login">ссылке.</a>

Ошибка чтения карты / карта повреждена. Это может произойти вследствие следующих причин: приложено несколько карт одновременно, механические повреждения карты (чипа или внутренней антенны), карту слишком быстро отвели от считывателя, в редких случаях проблема может быть вызвана технологической несовместимостью карты и считывателя. При отказе из-за ошибки чтения карты, повторите попытку оплаты этой картой еще раз.

Истек срок действия карты. Если срок действия Вашей карты истек, пожалуйста, обратитесь в банк для перевыпуска карты на новый срок действия или откройте новую бесконтактную карту.
'''

card_error_phone_answer = '''
<b>{question}</b>

Если Ваша карта в устройстве с технологией NFC не принимается для оплаты проезда на терминале, даже если Вы успешно расплачивались этой картой ранее, это может быть следствием следующих причин:

Ошибка чтения карты. При отказе из-за ошибки чтения карты, повторите попытку оплаты этой картой еще раз.

Истек срок действия карты. Если срок действия Вашей карты истек, пожалуйста, обратитесь в банк для перевыпуска карты на новый срок действия или откройте новую бесконтактную карту и привяжите ее к мобильному устройству.

Карта в стоп-листе. Это означает, что по данной карте была совершена поездка, за которую не произошло списание средств. Таким образом, поездка осталась неоплаченной, и по карте образовалась задолженность. Это может произойти из-за недостатка средств на карте на момент оплаты, блокировки карты банком или технических проблем при выполнении запроса на списание средств. Для вывода карты из стоп-листа при оплате токеном необходимо направить обращение на info@strelkacard.ru или обратиться на Горячую линию «Стрелка» 8 800 100-77-90
'''

card_debt_answer = '''
<b>{question}</b>

Если карта была использована для регистрации проезда, но по каким-то причинам списание средств не произошло, то карта автоматически попадает в стоп-лист транспортной системы. Карта не может быть использована в рамках транспортной системы до погашения задолженности по оплате проезда. При попытке регистрации проезда на экране терминала возникает сообщение «Карта в стоп-листе».

Списание суммы поездки с карты может не произойти по следующим причинам: отсутствие достаточного количества средств на карте, блокировка операций по карте банком-эмитентом или технические проблемы при выполнении запроса на списание средств.

В случае, если попытка списания с карты суммы в целях осуществления операций в рамках системы была неудачной, система автоматически продолжит попытки списания с карты суммы до достижения положительного результата.

Получить информацию о неоплаченных поездках, а также погасить задолженность можно в Личном кабинете пассажира.

Карта автоматически удаляется из стоп-листа в течение 10 минут с момента получения Оператором Системы информации от кредитной организации о погашении задолженности. Для использования такой карты в терминале перевозчик должен быть обеспечить актуализацию стоп-листа.
'''
