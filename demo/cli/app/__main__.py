import traceback

import accelbyte_py_sdk
import accelbyte_py_sdk.services.auth as auth_service
import accelbyte_py_sdk.api.iam as iam_service

from client.config import get_config
from client.demo import PlatformDataUnit

def start_testing(user_info, config, category_path="/python_lootbox_roll_plugin_demo"):
    pdu = PlatformDataUnit(
        user_info=user_info, 
        config=config, 
        currency_code="USDT1"
    )
    try:
        # 1.
        print("Configuring platform service grpc target... ")
        error = pdu.set_platform_service_grpc_target()
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")
        
        # 2.
        print("Creating store... ")
        error = pdu.creat_store()
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 3.
        print("Creating category... ")
        error = pdu.create_category(category_path)
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 4.
        print(f"Setting up currency ({pdu.currency_code})... ")
        error = pdu.create_currency()
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 5.
        print("Creating lootbox item(s)... ")
        items, error = pdu.create_lootbox_items(1, 5, category_path, True)
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")

        # 6.
        print(f"Granting item entitlement to user {user_info.user_name}... ")
        entitlement_id, error = pdu.grant_entitlement(user_info.user_id, items[0].id, 1)
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")
        print(f"\tEntitlement ID: {entitlement_id}\n")

        # 7.
        print("Consuming entitlement... ")
        lootbox_item_result, error = pdu.consume_item_entitlement(user_info.user_id, entitlement_id, 2)
        if error:
            print("[ERR]")
            raise Exception(error)
        print("[OK]")
        lootbox_item_result.write_to_console("    ")
        print("[SUCCESS]")
    except:
        print(traceback.format_exc())
        print("\n[FAILED]")
    finally:
        print("# Cleaning Up")
        print("## Deleting currency...")
        error = pdu.delete_store()
        if error:
            return
        print("[OK]")
        
        if config.GRPCServerURL:
            error = pdu.unset_platform_service_grpc_target()
            if error:
                print("failed to unset platform service grpc plugin url")
                return
        print("[CLEAN UP FINISHED]")

def main():
    config = get_config()

    accelbyte_py_sdk.initialize()

    print("# Arrange")
    print("## Login to AccelByte... ")
    _, error = auth_service.login_user(username=config.ABUsername, password=config.ABPassword)
    if error:
        raise Exception(error)
    print("[OK]")

    print("## Get user info")
    user_info, error = iam_service.public_get_my_user_v3() 
    if error:
        raise Exception(error)
    print("[OK]")
    
    print("# Test Start")
    start_testing()
            
if __name__ == "__main__":
    main()