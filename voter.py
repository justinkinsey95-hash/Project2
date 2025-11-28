class Voter:
    def __init__(self, id, party, opt_in):
        self.__voter_id = id
        self.__party = party
        self.__opt_in = opt_in

    def get_voter_id(self) -> str:
        """
        gets the voter's id number
        :return: the voter's id number as a string
        """
        return self.__voter_id

    def get_party(self) -> str:
        """
        gets the voter's party
        :return: the voter's party as a string
        """
        return self.__party

    def get_opt_in(self) -> str:
        """
        gets the voter's opt_in choice
        :return: string "Yes" or "No"
        """
        return self.__opt_in