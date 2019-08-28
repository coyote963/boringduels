
CREATE TABLE Players (
    SteamId varchar(18) PRIMARY KEY,
    DiscordId varchar(18) NOT NULL,
    Rating int DEFAULT 1000,
    RoundsPlayed int DEFAULT 0,
    DateCreated timestamp DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Sessions (
	SessionId INTEGER NOT NULL PRIMARY KEY,
	Map varchar(20),
	DateCreated timestamp DEFAULT CURRENT_TIMESTAMP,
	TimeEnding timestamp,
	UscPlayer varchar(18) NOT NULL,
	ManPlayer varchar(18) NOT NULL,
	FOREIGN KEY(UscPlayer) REFERENCES Players(SteamId),
	FOREIGN KEY(ManPlayer) REFERENCES Players(SteamId)
);

CREATE TABLE Kills (
	Killer varchar(18) NOT NULL,
	Victim varchar(18) NOT NULL,
	DateCreated timestamp DEFAULT CURRENT_TIMESTAMP,
	Weapon varChar(16) NOT NULL,
	Session INTEGER NOT NULL,
	FOREIGN KEY(Killer) REFERENCES Players(SteamId),
	FOREIGN KEY(Victim) REFERENCES Players(SteamId),
	FOREIGN KEY(Session) REFERENCES Sessions(SessionId)
)