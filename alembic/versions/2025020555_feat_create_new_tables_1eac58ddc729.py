"""feat: create new tables

Revision ID: 1eac58ddc729
Revises: 05c9a5a52630
Create Date: 2025-02-05 15:55:35.327266

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "1eac58ddc729"
down_revision = "05c9a5a52630"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.drop_constraint(
        "unique_sessionid_session", "session_screening_status", type_="unique"
    )
    op.create_unique_constraint(
        "unique_sessionid_session", "session_screening_status", ["session_id"]
    )
    op.drop_column("session_screening_status", "ens_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "orgdata",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column(
            "orgname", sa.VARCHAR(length=100), autoincrement=False, nullable=False
        ),
        sa.Column(
            "orgidentifier", sa.VARCHAR(length=100), autoincrement=False, nullable=False
        ),
        sa.Column("bvdids", sa.VARCHAR(length=100), autoincrement=False, nullable=True),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name="orgdata_pkey"),
        sa.UniqueConstraint("bvdids", name="orgdata_bvdids_key"),
        sa.UniqueConstraint("orgidentifier", name="orgdata_orgidentifier_key"),
    )
    # ### end Alembic commands ###
