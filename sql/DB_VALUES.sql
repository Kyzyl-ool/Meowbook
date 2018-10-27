DELETE FROM "Chat";
DELETE FROM "User";

INSERT INTO "Chat" VALUES (0, TRUE, 'Sample topic', 0);

INSERT INTO "User" VALUES (0, 'root', 'Koren');
INSERT INTO "User" VALUES (1, 'nonroot', 'NeKoren');