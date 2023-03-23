"""empty message

Revision ID: 7af4236350fd
Revises: 
Create Date: 2022-05-08 17:03:42.243609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7af4236350fd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('about_you',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prefix', sa.Text(), nullable=False),
    sa.Column('place_holder', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('analytics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('visits', sa.Integer(), nullable=True),
    sa.Column('profile_readme', sa.Integer(), nullable=True),
    sa.Column('project_readme', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_analytics_date'), 'analytics', ['date'], unique=False)
    op.create_table('skills',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('badge_link', sa.Text(), nullable=False),
    sa.Column('badge_type', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_skills_badge_type'), 'skills', ['badge_type'], unique=False)
    op.create_table('social_medias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('social_link', sa.Text(), nullable=False),
    sa.Column('badge_link', sa.Text(), nullable=False),
    sa.Column('badge_type', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_social_medias_badge_type'), 'social_medias', ['badge_type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_social_medias_badge_type'), table_name='social_medias')
    op.drop_table('social_medias')
    op.drop_index(op.f('ix_skills_badge_type'), table_name='skills')
    op.drop_table('skills')
    op.drop_index(op.f('ix_analytics_date'), table_name='analytics')
    op.drop_table('analytics')
    op.drop_table('about_you')
    # ### end Alembic commands ###
