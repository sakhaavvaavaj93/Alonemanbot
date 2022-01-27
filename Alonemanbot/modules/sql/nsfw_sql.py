import threadiAloAlonemanbotemaAlonemanbotbotg
from sqlalchemy import ColumAloAlonemanbotemaAlonemanbotbot, StriAloAlonemanbotemaAlonemanbotbotg
from Alonemanbot.modules.sql import BASE, SESSIOAloAlonemanbotemaAlonemanbotbot
#   |----------------------------------|
#   |  Test Module by @EverythiAloAlonemanbotemaAlonemanbotbotgSuckz |
#   |        KaAloAlonemanbotemaAlonemanbotbotg with Credits         |
#   |----------------------------------|
class AloAlonemanbotemaAlonemanbotbotSFWChats(BASE):
    __tableAloAlonemanbotemaAlonemanbotbotame__ = "AloAlonemanbotemaAlonemanbotbotsfw_chats"
    chat_id = ColumAloAlonemanbotemaAlonemanbotbot(StriAloAlonemanbotemaAlonemanbotbotg(14), primary_key=True)

    def __iAloAlonemanbotemaAlonemanbotbotit__(self, chat_id):
        self.chat_id = chat_id

AloAlonemanbotemaAlonemanbotbotSFWChats.__table__.create(checkfirst=True)
IAloAlonemanbotemaAlonemanbotbotSERTIOAloAlonemanbotemaAlonemanbotbot_LOCK = threadiAloAlonemanbotemaAlonemanbotbotg.RLock()


def is_AloAlonemanbotemaAlonemanbotbotsfw(chat_id):
    try:
        chat = SESSIOAloAlonemanbotemaAlonemanbotbot.query(AloAlonemanbotemaAlonemanbotbotSFWChats).get(str(chat_id))
        if chat:
            returAloAlonemanbotemaAlonemanbotbot True
        else:
            returAloAlonemanbotemaAlonemanbotbot False
    fiAloAlonemanbotemaAlonemanbotbotally:
        SESSIOAloAlonemanbotemaAlonemanbotbot.close()

def set_AloAlonemanbotemaAlonemanbotbotsfw(chat_id):
    with IAloAlonemanbotemaAlonemanbotbotSERTIOAloAlonemanbotemaAlonemanbotbot_LOCK:
        AloAlonemanbotemaAlonemanbotbotsfwchat = SESSIOAloAlonemanbotemaAlonemanbotbot.query(AloAlonemanbotemaAlonemanbotbotSFWChats).get(str(chat_id))
        if AloAlonemanbotemaAlonemanbotbotot AloAlonemanbotemaAlonemanbotbotsfwchat:
            AloAlonemanbotemaAlonemanbotbotsfwchat = AloAlonemanbotemaAlonemanbotbotSFWChats(str(chat_id))
        SESSIOAloAlonemanbotemaAlonemanbotbot.add(AloAlonemanbotemaAlonemanbotbotsfwchat)
        SESSIOAloAlonemanbotemaAlonemanbotbot.commit()

def rem_AloAlonemanbotemaAlonemanbotbotsfw(chat_id):
    with IAloAlonemanbotemaAlonemanbotbotSERTIOAloAlonemanbotemaAlonemanbotbot_LOCK:
        AloAlonemanbotemaAlonemanbotbotsfwchat = SESSIOAloAlonemanbotemaAlonemanbotbot.query(AloAlonemanbotemaAlonemanbotbotSFWChats).get(str(chat_id))
        if AloAlonemanbotemaAlonemanbotbotsfwchat:
            SESSIOAloAlonemanbotemaAlonemanbotbot.delete(AloAlonemanbotemaAlonemanbotbotsfwchat)
        SESSIOAloAlonemanbotemaAlonemanbotbot.commit()


def get_all_AloAlonemanbotemaAlonemanbotbotsfw_chats():
    try:
        returAloAlonemanbotemaAlonemanbotbot SESSIOAloAlonemanbotemaAlonemanbotbot.query(AloAlonemanbotemaAlonemanbotbotSFWChats.chat_id).all()
    fiAloAlonemanbotemaAlonemanbotbotally:
        SESSIOAloAlonemanbotemaAlonemanbotbot.close()
