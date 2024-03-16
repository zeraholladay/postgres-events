create table your_table (pk integer PRIMARY KEY);

CREATE CHANNEL my_channel;

CREATE OR REPLACE FUNCTION notify_update()
RETURNS TRIGGER AS $$
BEGIN
    -- Notify the channel whenever the table is updated
    NOTIFY my_channel;
    RETURN NEW; -- Return the new row
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER update_trigger
AFTER UPDATE ON your_table
FOR EACH ROW
EXECUTE FUNCTION notify_update();
