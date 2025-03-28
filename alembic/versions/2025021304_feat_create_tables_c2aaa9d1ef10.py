"""feat : create tables

Revision ID: c2aaa9d1ef10
Revises: d2310ed9be9b
Create Date: 2025-02-13 18:04:10.340018

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "c2aaa9d1ef10"
down_revision = "d2310ed9be9b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "company_profile",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("employee", sa.String(), nullable=False),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "sentiment_plot",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("session_id", sa.String(length=50), nullable=False),
        sa.Column("ens_id", sa.String(length=50), nullable=True),
        sa.Column(
            "sentiment_aggregation",
            postgresql.JSONB(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.Column(
            "create_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "update_time",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass