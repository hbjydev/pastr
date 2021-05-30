-- upgrade --
ALTER TABLE "pastes" ADD "private" BOOL NOT NULL  DEFAULT False;
-- downgrade --
ALTER TABLE "pastes" DROP COLUMN "private";
