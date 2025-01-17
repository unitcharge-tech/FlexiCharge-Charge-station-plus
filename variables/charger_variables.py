from sre_parse import State
from StateHandler import States
class Charger():

    CHARGE_TIME_MAX = 101

    def __init__(self):
        # Charger variables
        self._is_charging = False
        self._charging_id_tag = None
        self._charging_connector = None
        self._charger_id = 000000
        self._charging_Wh = 0  # I think this is how many Wh have been used to charge
        self._charging_Wh_per_second = 0.3
        self._charging_price = 0.0
        self._current_charging_percentage = 0
        self._current_charge_time_left = self.CHARGE_TIME_MAX
        self._meter_value_total = 0 
        self._status = "Available"
        self._state = States.S_STARTUP
    # Get for charging variables

    @property
    def charging_Wh(self):
        return self._charging_Wh
    @property
    def charging_price(self):
        return self.charging_price

    @property
    def is_charging(self):
        return self._is_charging

    @property
    def charging_id_tag(self):
        return self._charging_id_tag

    @property
    def charging_connector(self):
        return self._charging_connector

    @property
    def current_charging_percentage(self):
        return self._current_charging_percentage
        
    @property    
    def current_charge_time_left(self):
        return self._current_charge_time_left

    @property
    def charger_id(self):
        return self._charger_id

    @property    
    def current_state(self):
        return self._state

    @property
    def charging_Wh_per_second(self):
        return self._charging_Wh_per_second

     # Set for charging variables

    @charging_Wh.setter
    def charging_Wh(self, Wh: int):
        self._charging_Wh = Wh
    @charging_price.setter
    def charging_price(self, price: float):
        self._charging_price = price

    @is_charging.setter
    def is_charging(self, boolean: bool):
        self._is_charging = boolean

    @current_state.setter
    def current_state(self, state: States):
        self._state = state   

    @charging_Wh_per_second.setter
    def charging_Wh_per_second(self, value):
        self._charging_Wh_per_second = value

    @charger_id.setter
    def charger_id(self, id):
        self._charger_id = id

    @charging_id_tag.setter
    def charging_id_tag(self, charging_id_tag):
        self._charging_id_tag = charging_id_tag

    @charging_connector.setter
    def charging_connector(self, charging_connector):
        self._charging_connector = charging_connector

    @current_charging_percentage.setter
    def current_charging_percentage(self, value):
        self._current_charging_percentage = value

    @current_charge_time_left.setter
    def current_charge_time_left(self, value):
        self._current_charge_time_left = value

    # Get for misc variables
    @property
    def meter_value_total(self):
        return self._meter_value_total

    # Set for misc variables
    @meter_value_total.setter
    def increment_meter_value_total_by(self, value: int):  # increment variable
        self._meter_value_total += value

    @property
    def meter_value_total(self):
        return self._meter_value_total

    @property
    def status(self):
        return self._status

    # Set for misc variables
    @meter_value_total.setter
    def increment_meter_value_total_by(self, value: int):  # increment variable
        self._meter_value_total += value

    @status.setter
    def status(self, status):
        self._status = status
