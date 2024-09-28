class VirtualMachine:
    def __init__(self, name, os, ram, cpu, storage):
        self.name = name
        self.os = os
        self.ram = ram
        self.cpu = cpu
        self.storage = storage
        self.status = "Offline"

    def start(self):
        self.status = "Running"
        print(f"{self.name} started successfully.")

    def stop(self):
        self.status = "Offline"
        print(f"{self.name} stopped successfully.")

    def restart(self):
        self.stop()
        self.start()

class VDIManager:
    def __init__(self):
        self.vms = {}

    def add_vm(self, vm):
        self.vms[vm.name] = vm
        print(f"VM '{vm.name}' added successfully.")
    def remove_vm(self, name):
        if name in self.vms:
            del self.vms[name]
            print(f"VM '{name}' removed successfully.")
        else:
            print(f"VM '{name}' not found.")

    def list_vms(self):
        print("Virtual Machines:")
        for vm in self.vms.values():
            print(f"{vm.name} - {vm.os} - {vm.status}")

    def manage_vm(self, name):
        if name in self.vms:
            vm = self.vms[name]
            print(f"Managing VM '{name}':")
            print("1. Start")
            print("2. Stop")
            print("3. Restart")
            choice = input("Enter choice: ")
            if choice == "1":
                vm.start()
            elif choice == "2":
                vm.stop()
            elif choice == "3":
                vm.restart()
            else:
                print("Invalid choice.")
        else:
            print(f"VM '{name}' not found.")
    def main():
         vdi_manager = VDIManager()

    while True:
        print("VDI Manager")
        print("1. Add VM")
        print("2. Remove VM")
        print("3. List VMs")
        print("4. Manage VM")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter VM name: ")
            os = input("Enter OS: ")
            ram = input("Enter RAM: ")
            cpu = input("Enter CPU: ")
            storage = input("Enter storage: ")
            vm = VirtualMachine(name, os, ram, cpu, storage)
            vdi_manager.add_vm(vm)
        elif choice == "2":
            name = input("Enter VM name: ")
            vdi_manager.remove_vm(name)
        elif choice == "3":
            vdi_manager.list_vms()
        elif choice == "4":
            name = input("Enter VM name: ")
            vdi_manager.manage_vm(name)
        elif choice == "5":
              break
        else:
            print("Invalid choice.")

       if __name__ == "__main__":
             main()



