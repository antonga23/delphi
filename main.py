import flask
import flask_restful
import twint

def main() :
    # Configure
    c = twint.Config()
    c.Username = "realDonaldTrump"
    c.Search = "great"

    # Run
    twint.run.Search(c)


if __name__ == "__main__":
    main()