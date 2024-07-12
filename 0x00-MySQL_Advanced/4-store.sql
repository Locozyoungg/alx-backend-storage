-- Script to create a trigger that decreases the quantity of an item after adding a new order

-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS decrease_quantity;

-- Create the trigger
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;

