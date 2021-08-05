--
-- program2.lua
--
-- Authors: Artur Barichello
--          Lucas Verdade
--          Lucas Zacchi

int max_length;
max_length = 5;

string product_name;
product_name = new string[max_length];

string product_description;
product_description = new string[max_length];

float product_price;
product_price = new float[max_length];

-- auxiliar function that put a empty slot on {index} position
def erase_index(int index){
    if (index >= max_length){
        if (index < 0){
            print("[ERROR] Invalid product index! Index should be between 0 and "+ string(max_length));
        } else {
            product_name[index] = "empty";
            product_description[index] = "empty";
            product_price[index] = -1.0;
            print("[LOG] Position "+index+" erased.");
        }
    } else {
        product_name[index] = "empty";
        product_description[index] = "empty";
        product_price[index] = -1.0;
        print("[LOG] Position "+index+" erased.");
    }
    
    return;
}

-- initalizing empty slots
int j;
for (j=0; j < max_length; j = j + 1){
    erase_index(j);
}

-- print all informations about the product in index position
-- if index is not a valid position then print error
def product_info(int p_index){
    if (p_index >= 0){
        if (p_index < max_length){
            print("Product: "+ string(p_index));
            print("Name: " + product_name[p_index]);
            print("Description: " + product_description[p_index]);
            print("Price: $" + string(product_price[p_index]));
        } else {
            print("[ERROR] Invalid product index! Index should be between 0 and "+ string(max_length));
        }
    } else {
        print("[ERROR] Invalid product index! Index should be between 0 and "+ string(max_length));
    }
        
    return;
}

-- check if there is any available slots and then
def add_product(string name, string description, float price){
    int i;
    int empty_slot;
    empty_slot = -1;

    -- searching for slot
    for (i = 0; i < max_length; i = i + 1){
        if (product_name[i] == "empty"){
            print("Empty slot found");
            empty_slot = i;
        }
    }

    if (empty_slot <= -1){ -- case there is not an empty slot
        print("[ERROR] There is not an empty slot to add a product!");
        return;

    } else { -- case there is an empty slot available
        print("[LOG] Adding product...");
        product_name[product_index] = name;
        product_description[product_index] = description;
        product_price[product_index] = price;
        print("[SUCCESS] Product Added!");
    }
}

-- TODO: update function
def update_product(string name, string new_name, float new_price, string new_description){
    -- checking if exists
    int i;
    int product_index;
    product_index = -1;
    
    print("[LOG] Searching for product which name is: '"+ name + "' ...");
    for (i = 0; i < max_length; i = i + 1){
        if (product_name[i] == name){
            print("Product:" + name + " found in position "+ i);
            product_index = i;
        }
    }

    -- handle error
    if (product_index <= -1){
        print("[ERROR] Product not found. Are you sure that the product name is: "+ name);
    } else {
       -- handle update
       print("[LOG] Updating...");
       product_name[product_index] = new_name;
       product_description[product_index] = new_description;
       product_price[product_index] = new_price;
       print("[SUCCESS] Update done!");
    }
    return;
}

-- Delete algorithm:
--  Search for product
--  If finds it then calls erase_index and delete that position
--  If does not find then print error
def delete_product(string name){
    -- checking if exists
    int i;
    int product_index;
    product_index = -1;
    
    print("[LOG] Searching for product which name is: '"+ name + "' ...");
    for (i = 0; i < max_length; i = i + 1){
        if (product_name[i] == name){
            print("Product:" + name + " found in position "+ i);
            product_index = i;
        }
    }

    -- handle error
    if (product_index <= -1){
        print("[ERROR] Product not found. Are you sure that the product name is: "+ name);
    } else {
       -- handle delete 
       print("[LOG] Deleting...");
       erase_index(product_index);
    }
    return;
}

-- main
--  add 5 products
--  try to add one more
--  remove something
--  update something else
def main(){
    -- Adding 5 products
    add_product("programming in lua, book", "This book is a detailed and authoritative introduction to all aspects of Lua programming written by Lua's chief architect. ", 156.0);
    add_product("laptop", "laptop lenovo ideapad s145", 2500.0);
    add_product("echo dot third gen", "Amazon voice-controlled smart speaker that uses an artificially intelligent personal assistant", 250.0);
    add_product("guitar", "giannini acoustic guitar 6 strings",1000.0);
    add_product("moto g","Motorola Moto G with cracked screen", 800.0);

    -- Trying to add
    add_product("overflow", "Overflow test, this should not be added", 1.0);

    -- Free some space
    delete_product("laptop");

    -- Update product
    update_product("guitar", "acoustic guitar", "giannini acoustic guitar 6 strings", 1200.0);

    return;
}

-- run
main();