from mycroft import MycroftSkill, intent_file_handler


class AwardCoverage(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('coverage.award.intent')
    def handle_coverage_award(self, message):
        self.speak_dialog('coverage.award')


def create_skill():
    return AwardCoverage()

