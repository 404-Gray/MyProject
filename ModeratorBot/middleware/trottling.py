import asyncio
from aiogram import types, Dispatcher
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import Throttled


class ThrottlingMiddleware(BaseMiddleware):
    """
    Простое промежуточное программное обеспечение
    """

    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood'):
        self.rate_limit = limit
        self.prefix = key_prefix
        super(ThrottlingMiddleware, self).__init__()

    async def on_process_message(self, message: types.Message, data: dict):

        """
        Этот обработчик вызывается, когда диспетчер получает сообщение

        :param message:
        """
        # Получить текущий хэндлер

        handler = current_handler.get()

        # Получить диспетчер из контекста
        dispatcher = Dispatcher.get_current()
        # Если обработчик был настроен, получите ограничение скорости и ключ от обработчика
        if handler:
            limit = getattr(handler, 'throttling_rate_limit', self.rate_limit)
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            limit = self.rate_limit
            key = f"{self.prefix}_message"

        # Используйте метод Dispatcher.throttle.
        try:
            await dispatcher.throttle(key, rate=limit)
        except Throttled as t:
            # Выполнить действие
            await self.message_throttled(message, t)

            # Отменить текущий обработчик
            raise CancelHandler()


    async def message_throttled(self, message: types.Message, throttled: Throttled):
        """
    Уведомлять пользователя только при первом превышении и уведомлять о разблокировке только при последнем превышении

        :param message:
        :param throttled:
    """
        handler = current_handler.get()
        dispatcher = Dispatcher.get_current()
        if handler:
            key = getattr(handler, 'throttling_key', f"{self.prefix}_{handler.__name__}")
        else:
            key = f"{self.prefix}_message"

        # Подсчитать, сколько времени осталось до завершения блока
        delta = throttled.rate - throttled.delta

        # Предотвращение флуда
        if throttled.exceeded_count <= 5:
            await message.reply('Слишком много запросов!')

        # Спящий режим.
        await asyncio.sleep(delta)

        # Проверка состояния блокировки
        thr = await dispatcher.check_key(key)

        # Если текущее сообщение не является последним с текущим ключом - не отправлять сообщение
        if thr.exceeded_count == throttled.exceeded_count:
            await message.reply('Разблокирован.')
