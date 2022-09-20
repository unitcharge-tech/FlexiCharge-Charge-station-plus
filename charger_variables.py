
class Charger():
    def __init__(self):
        # Charger variables
        self.is_charging = False
        self.charging_id_tag = None
        self.charging_connector = None
        self.charger_id = 000000
        self.charging_Wh = 0  # I think this is how many Wh have been used to charge
        self.current_charging_percentage = 0
    # Get for charging variables

    @property
    def charging_Wh(self):
        return self.charging_Wh

    @property
    def is_charging(self):
        return self.is_charging

    @property
    def charging_id_tag(self):
        return self.charging_id_tag

    @property
    def charging_connector(self):
        return self.charging_connector

    @property
    def current_charging_percentage(self):
        return self.current_charging_percentage

    @property
    def charger_id(self):
        return self.charger_id

     # Set for charging variables

    @charging_Wh.setter
    def charging_Wh(self, Wh: int):
        self.charging_Wh = Wh

    @is_charging.setter
    def is_charging(self, boolean: bool):
        self.is_charging = boolean

    @charger_id.setter
    def charger_id(self, id):
        self.charger_id = id

    @charging_id_tag.setter
    def charging_id_tag(self, charging_id_tag):
        self.charging_id_tag = charging_id_tag

    @charging_connector.setter
    def charging_connector(self, charging_connector):
        self.charging_connector = charging_connector

    @current_charging_percentage.setter
    def increment_current_charging_percentage_by(self, value: int):
        self.current_charging_percentage += value
