
""" 
     # Reservation related variables

     ReserveConnectorZeroSupported = True
     """


class Get():
    def __init__(self):
        self.reserved_connector = None
        self.reserve_now_timer = 0
        self.is_reserved = False
        self.reservation_id_tag = None
        self.reservation_id = None

        self.meter_value_total = 0
        self.current_charging_percentage = 0

        # Charger variables
        self.is_charging = False
        self.charging_id_tag = None
        self.charging_connector = None
        self.charger_id = 000000
        self.charging_Wh = 0  # I think this is how many Wh have been used to charge

        # UI variables

    # Get for charging variables

    def charging_Wh(self):
        return self.charging_Wh

    def is_charging(self):
        return self.is_charging

    def charging_id_tag(self):
        return self.charging_id_tag

    def charging_connector(self):
        return self.charging_connector

    def current_charging_percentage(self):
        return self.current_charging_percentage

    def charger_id(self):
        return self.charger_id

    # Get for reservation variables
    def is_reserved(self):
        return self.is_reserved

    def reservation_id_tag(self):
        return self.reservation_id_tag

    def reservation_id(self):
        return self.reservation_id

    def reserved_connector(self):
        return self.reserved_connector

    def reserve_now_timer(self):
        return self.reserve_now_timer

    # Get for misc variables
    def meter_value_total(self):
        return self.meter_value_total

    # Get UI variables


class Set():
    # Set for charging variables
    def charging_Wh(self, Wh: int):
        self.charging_Wh = Wh

    def is_charging(self, boolean: bool):
        self.is_charging = boolean

    def charger_id(self, id):
        self.charger_id = id

    def charging_id_tag(self, charging_id_tag):
        self.charging_id_tag = charging_id_tag

    def charging_connector(self, charging_connector):
        self.charging_connector = charging_connector

    def increment_current_charging_percentage_by(self, value: int):
        self.current_charging_percentage += value

    # Set for reservation variables

    def is_reserved(self, boolean: bool):
        self.is_reserved = boolean

    def reservation_id_tag(self, reservation_id_tag):
        self.reservation_id_tag = reservation_id_tag

    def reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    def reserved_connector(self, reserved_connector):
        self.reserved_connector = reserved_connector

    def reserve_now_timer(self, reserved_now_timer):
        self.reserve_now_timer = reserved_now_timer

    def decrement_reserve_now_timer_by(self, time: int):
        self.reserve_now_timer -= time

    # Set for misc variables

    def increment_meter_value_total_by(self, value: int):  # increment variable
        self.meter_value_total += value

    # Set UI variables
