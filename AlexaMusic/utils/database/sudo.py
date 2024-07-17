from typing import Dict, List, Union

from AlexaMusic.core.mongo import mongodb

sudoersdb = db.sudoers
paidsubsdb = db.paidsubs


async def get_sudoers() -> list:
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    if not sudoers:
        return []
    return sudoers["sudoers"]


async def add_sudo(user_id: int) -> bool:
    sudoers = await get_sudoers()
    sudoers.append(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True


async def remove_sudo(user_id: int) -> bool:
    sudoers = await get_sudoers()
    sudoers.remove(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True


#my code======================

async def get_subs() -> list:
    subscribers = await paidsubs.find_one({"sudo": "sudo"})
    if not subscribers:
        return []
    return subscribers["subscribers"]


async def add_sudo(user_id: int) -> bool:
    subscribers = await get_subs()
    subscribers.append(user_id)
    await paidsubs.update_one(
        {"sudo": "sudo"}, {"$set": {"subscribers": subscribers}}, upsert=True
    )
    return True


async def remove_sudo(user_id: int) -> bool:
    subscribers = await get_subs()
    subscribers.remove(user_id)
    await paidsubs.update_one(
        {"sudo": "sudo"}, {"$set": {"subscribers": subscribers}}, upsert=True
    )
    return True
