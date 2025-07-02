class Command:
    def execute(self, player):
        raise NotImplementedError()

class MoveLeftCommand(Command):
    def execute(self, player):
        player.move_left()

class MoveRightCommand(Command):
    def execute(self, player):
        player.move_right()

class JumpCommand(Command):
    def execute(self, player):
        player.jump()
