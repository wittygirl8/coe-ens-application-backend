"""feat : updation

Revision ID: dddd09b4cdab
Revises: ed93ff304032
Create Date: 2025-02-15 10:40:17.741060

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "dddd09b4cdab"
down_revision = "ed93ff304032"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "news_master",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("title", sa.Text(), nullable=True),
        sa.Column("category", sa.Text(), nullable=True),
        sa.Column("summary", sa.Text(), nullable=True),
        sa.Column("news_date", sa.Date(), nullable=True),
        sa.Column("link", sa.Text(), nullable=True),
        sa.Column("sentiment", sa.String(), nullable=True),
        sa.Column("content_filtered", sa.Boolean(), nullable=True),
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
    
    op.add_column(
        "company_profile", sa.Column("session_id", sa.String(length=50), nullable=False)
    )
    op.add_column(
        "company_profile", sa.Column("ens_id", sa.String(length=50), nullable=True)
    )
    

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass