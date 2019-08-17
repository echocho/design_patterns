class Memento(object):
    def __init__(self, state):
        self._state = state

    def get_last_saved_state(self):
        return self._state


class Originator(object):
    _state = ""

    def set(self, state):
        print(f"Originator: setting state to {state}")
        self._state = state

    def save_state(self):
        print("Originator: saving to Memento")
        return Memento(self._state)

    def restore_state(self, memento):
        print(f"Originator: restoring from Memento: {self._state}")
        self._state = memento.get_last_saved_state()


saved_states = []
originator = Originator()
originator.set("State1")
originator.set("State2")
saved_states.append(originator.save_state())

originator.set("State3")
saved_states.append(originator.save_state())

originator.set("State4")

originator.restore_state(saved_states[0])
