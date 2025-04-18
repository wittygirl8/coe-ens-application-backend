"""refactor: new comdification

Revision ID: f004c2904592
Revises: 70545916e22f
Create Date: 2025-02-14 13:29:11.431798

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "f004c2904592"
down_revision = "70545916e22f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "report_plot",
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
    op.drop_table("sentiment_plot")

    op.alter_column(
        "company_profile", "name", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column(
        "company_profile", "location", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column(
        "company_profile", "address", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column(
        "company_profile", "website", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column(
        "company_profile", "active_status", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column(
        "company_profile", "operation_type", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column(
        "company_profile", "legal_status", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column(
        "company_profile",
        "national_identifier",
        existing_type=sa.VARCHAR(),
        nullable=True,
    )
    op.alter_column(
        "company_profile",
        "alias",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        nullable=True,
    )
    op.alter_column(
        "company_profile",
        "incorporation_date",
        existing_type=sa.DATE(),
        type_=sa.String(),
        nullable=True,
    )
    op.alter_column(
        "company_profile",
        "shareholders",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        nullable=True,
    )
    op.alter_column(
        "company_profile", "revenue", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column(
        "company_profile", "subsidiaries", existing_type=sa.VARCHAR(), nullable=True
    )
    op.alter_column(
        "company_profile",
        "corporate_group",
        existing_type=sa.NUMERIC(),
        type_=sa.String(),
        nullable=True,
    )
    op.alter_column(
        "company_profile",
        "key_executives",
        existing_type=sa.VARCHAR(),
        type_=sa.Text(),
        nullable=True,
    )
    op.alter_column(
        "company_profile", "employee", existing_type=sa.VARCHAR(), nullable=True
    )
    

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass