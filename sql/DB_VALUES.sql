DELETE FROM "Chat";
DELETE FROM "User";
DELETE FROM "Message";
DELETE FROM "Member";

INSERT INTO "User" VALUES (0, 'TestUser', 'TestNickname');
INSERT INTO "Chat" VALUES (0, TRUE, 'Sample topic', NULL);
INSERT INTO "Message" VALUES (0, 0, 0, 'Hello', '2018-11-11 11:11:11');
INSERT INTO "Member" VALUES (0, 0, 0, 1);


